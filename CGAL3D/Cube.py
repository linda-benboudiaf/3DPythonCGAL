# Import des librairie de modelisation
from CGAL.CGAL_Polyhedron_3 import Polyhedron_3
from CGAL.CGAL_Kernel import Point_3

# Definition de la fonction qui forme un cube ...
def cube(P):
  # appends a cube of size [0,1]^3 to the polyhedron P.
  #is_valid() methode natif de python
  assert P.is_valid()
  h = P.make_tetrahedron(Point_3( 1, 0, 0),Point_3( 0, 0, 1),Point_3( 0, 0, 0),Point_3( 0, 1, 0))
  g = h.next().opposite().next()
  P.split_edge( h.next() )
  P.split_edge( g.next() )
  P.split_edge( g )
  h.next().vertex().set_point( Point_3( 1, 0, 1) )
  g.next().vertex().set_point( Point_3( 0, 1, 1) )
  g.opposite().vertex().set_point( Point_3( 1, 1, 0) )
  f = P.split_facet(g.next(),g.next().next().next())
  e = P.split_edge(f)
  e.vertex().set_point( Point_3( 1, 1, 1) )
  P.split_facet( e, f.next().next())
  assert P.is_valid()
  return h

# un polyédre objet solide sans suface arrondi ...
P = Polyhedron_3()
h = cube(P)
assert not P.is_tetrahedron(h)