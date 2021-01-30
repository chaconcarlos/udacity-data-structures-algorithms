PATH_SEPARATOR = "/"

# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
  def __init__(self, root_handler, default_handler):
    # Initialize the trie with an root node and a handler, this is the root path or home page node
    self.root            = RouteTrieNode(root_handler)
    self.default_handler = default_handler

  def insert(self, route, handler):
    # Similar to our previous example you will want to recursively add nodes
    # Make sure you assign the handler to only the leaf (deepest) node of this path
    route_parts = route.strip(PATH_SEPARATOR).split(PATH_SEPARATOR)

    current_node = self.root

    for part in route_parts:
      part_node = current_node.find(part)

      if part_node is None:
        part_node = current_node.insert(part, self.default_handler)

      current_node = part_node

    current_node.handler = handler

  def find(self, route):
    # Starting at the root, navigate the Trie to find a match for this path
    # Return the handler for a match, or None for no match
    result_handler = self.default_handler

    if route == PATH_SEPARATOR:
      result_handler = self.root.handler
    else:
      route_parts = route.strip(PATH_SEPARATOR).split(PATH_SEPARATOR)
      current_node   = self.root

      for part in route_parts:
        current_node = current_node.find(part)

        if current_node is None:
          break

      if current_node:
        result_handler = current_node.handler

    return result_handler


# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
  def __init__(self, handler):
    # Initialize the node with children as before, plus a handler
    self.handler  = handler
    self.children = dict()

  def insert(self, route, handler):
    # Insert the node as before
    node = self.children.get(route)

    if node is None:
      node = RouteTrieNode(handler)
      self.children[route] = node
    else:
      node.handler = handler

    return node

  def find(self, route):
    return self.children.get(route)


# The Router class will wrap the Trie and handle
class Router:
  def __init__(self, root_handler, default_handler):
      # Create a new RouteTrie for holding our routes
      # You could also add a handler for 404 page not found responses as well!
      self.routes = RouteTrie(root_handler, default_handler)

  def add_handler(self, route, handler):
      # Add a handler for a path
      # You will need to split the path and pass the pass parts
      # as a list to the RouteTrie
      if not route:
        raise ValueError("'route' parameter can't be None or empty")

      if not handler:
        raise ValueError("'route' parameter can't be None or empty")

      self.routes.insert(route, handler)

  def lookup(self, route):
      # lookup path (by parts) and return the associated handler
      # you can return None if it's not found or
      # return the "not found" handler if you added one
      # bonus points if a path works with and without a trailing slash
      # e.g. /about and /about/ both return the /about handler
      if not route:
        raise ValueError("'route' parameter can't be None or empty")

      return self.routes.find(route)

# Here are some test cases and expected outputs you can use to test your implementation

# create the router and add a route
router = Router("root handler", "not found handler") # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about", "about handler")  # add a route
router.add_handler("/home/test/test2/test3/test4", "Test4!")  # add a route
router.add_handler("/home/test/test/test/test", "Duplicated route test success!!")  # add a route

# some lookups with the expected output

try:
  print(router.lookup(None)) # should throw ValueError
except ValueError as exception:
  print(exception)

try:
  print(router.lookup("")) # should throw ValueError
except ValueError as exception:
  print(exception)

print(router.lookup("/")) # should print 'root handler'
print(router.lookup("//")) # should print 'not found handler'
print(router.lookup("/home")) # should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about")) # should print 'about handler'
print(router.lookup("/home/about/")) # should print 'about handler' or None if you did not handle trailing slashes
print(router.lookup("/home/about/me")) # should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/test/test2/test3/test4")) # should print 'Test4!'
print(router.lookup("/home/test/test/test/test")) # should print 'Duplicated route test success!!'
