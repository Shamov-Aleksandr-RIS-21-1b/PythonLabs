from shapes import *

tr = Triangle(Point(0, 0), Point(4, 0), Point(0, 4))
rect = Rectangle(Point(4, 0), Point(0, 2), Point(-4, 0), Point(0, -2))
ell = Ellipse(Point(0, 0), 4, 5)

Jsoner.save(tr.get_json_data(), "Triangle")
Jsoner.save(rect.get_json_data(), "Rectangle")
Jsoner.save(ell.get_json_data(), "Ellipse")

Jsoner.show_all()

print(f"Triangle square: {tr.get_square()}")
print(f"Rectangle square: {rect.get_square()}")
print(f"Ellipse square: {ell.get_square()}")

rect = Rectangle.from_json(Jsoner.load("Rectangle"))
rect.points[3].y = -10
Jsoner.save(rect.get_json_data(), "Rectangle")
Jsoner.show_obj("Rectangle")