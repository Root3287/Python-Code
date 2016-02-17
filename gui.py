# GUI
# Timothy A. Gibbons
from graphics import *
import string;
import math;

running = True;
process =[];
obj = [];
def slope(x1,y1,x2,y2):
	return (y1-y2/x1-x2)*-1;
def distance(x1, y1, x2, y2):
	return math.sqrt( math.pow((x1-x2),2) + math.pow((y1-y2),2) )
def main():
	global running;
	global process;
	win = GraphWin("Canvas", 900, 900/16*9);

	while running:
		if(win.isClosed()):
			running = False
		if(win.isOpen()):
			command = input("Terminal "+ " ".join(process) +"$:");
			command = command.lower();
			command = command.split(" ");
			
			if(win.isClosed()):
				running = False
				break;

			if(command[0] == ""):
				print("Invalid Syntax! Type 'help' for help.");
			
			#list the help
			elif(command[0] == "help"):
				print(" quit - quit the process.\n exit - exit the window. \n square [size] - draws a square where the user clicks \n window - new window \n bullseye - draw a bullseye in the center of the screen.");
				
			#quit the current process
			elif(command[0] == "quit"):
				if(len(process) >= 1):
					if(process[0] is not None):
						process.pop()
	        
	        #exit the window			
			elif(command[0] == "exit"):
				running = False;
			
			#draw a square where the user clicks
			elif (command[0] == "square"):
				process.append("square");
				p1 = win.getMouse();
				if(len(command) >= 2):
					if(command[1] is not None):
						size = int(command[1]);
				else:
					size = 10;
				line01 = Line(p1, Point(p1.getX()+size, p1.getY() ));
				line02 = Line(p1, Point(p1.getX(), p1.getY()+size ));
				line03 = Line(Point(p1.getX(), p1.getY()+size), Point(p1.getX()+size, p1.getY()+size));
				line04 = Line(Point(p1.getX()+size, p1.getY()), Point(p1.getX()+size, p1.getY()+size));
				line01.draw(win);
				line02.draw(win);
				line03.draw(win);
				line04.draw(win);
				obj.append(line01)
				obj.append(line02)
				obj.append(line03)
				obj.append(line04)
				process.pop();
			#new Window
			elif(command[0] == "canvas"):
				win = GraphWin("Canvas", 900, 900/16*9);

			elif(command[0] == "bullseye"):
				circle01 = Circle(Point(900/2, 900/16*9/2), 100);
				circle02 = Circle(Point(900/2, 900/16*9/2), 80);
				circle03 = Circle(Point(900/2, 900/16*9/2), 60);
				circle04 = Circle(Point(900/2, 900/16*9/2), 40);
				circle05 = Circle(Point(900/2, 900/16*9/2), 20);
				circle02.setFill(color_rgb(0,0,0))
				circle03.setFill(color_rgb(0,0,255))
				circle04.setFill(color_rgb(255,0,0))
				circle05.setFill(color_rgb(255,255,0))
				circle01.draw(win);
				circle02.draw(win);
				circle03.draw(win)
				circle04.draw(win)
				circle05.draw(win)
				obj.append(circle01)
				obj.append(circle02)
				obj.append(circle03)
				obj.append(circle04)
				obj.append(circle05)
			elif(command[0] == "house"):
				p1 = win.getMouse()
				p2 = win.getMouse()
				p1b = Point(p2.getX(), p1.getY())
				p2b = Point(p1.getX(), p2.getY())
				body = Polygon(p1, p1b, p2, p2b );
				body.draw(win)
				obj.append(body)

				p3 = win.getMouse()
				p3b = Point(p3.getX()-((distance(p1.getX(), p1.getY(), p2b.getX(), p2b.getY())*1/5))/2, p3.getY())
				p3c = Point(p3.getX()+((distance(p1.getX(), p1.getY(), p2b.getX(), p2b.getY())*1/5))/2, p3.getY())
				doorHeightLine = Line(p3,p3c);
				doorHeightLine2 = Line(p3,p3b);
				doorSide = Line(p3b,Point(p3b.getX(), p1b.getY()));
				doorSide2 = Line(p3c, Point(p3c.getX(), p1b.getY()))
				doorSide.draw(win);
				doorSide2.draw(win)
				doorHeightLine.draw(win)
				doorHeightLine2.draw(win)
				obj.append(doorSide)
				obj.append(doorSide2)
				obj.append(doorHeightLine)
				obj.append(doorHeightLine2)

				p4 = win.getMouse()
				p4b = Point(p4.getX()+p3b.getX()/8, p4.getY()+p3b.getX()/8);
				p4c = Point(p4.getX()-p3b.getX()/8, p4.getY()-p3b.getX()/8);
				window = Rectangle(p4b, p4c)
				window.draw(win);
				obj.append(window)

				p5 = win.getMouse();
				roof = Line(p2b,p5);
				roof2= Line(p2, p5);
				roof.draw(win)
				roof2.draw(win)
				obj.append(roof)
				obj.append(roof2)
			elif(command[0] == "line"):
				p1 = win.getMouse()
				p2 = win.getMouse()
				print([p1.getX(), p1.getY(), p2.getX(), p2.getY()])
				line = Line(p1, p2)
				if(len(command) >= 2):
					if(command[1] == "-d"):
						line.draw(win)
						print("Slope: ", slope(p1.getX(),p1.getY(),p2.getX(),p2.getY())," distance: ", distance(p1.getX(), p1.getY(), p2.getX(), p2.getY()));
						obj.append(line);
				else:
					line.draw(win)
					obj.append(line)
			elif(command[0] == "face"):
				p1 = win.getMouse();
				p2 = win.getMouse();
				oval = Oval(p1, p2);
				oval.draw(win)
				obj.append(win)

				p3 = win.getMouse();
				p4 = win.getMouse();
				p3a = Point(p3.getX()-50, p3.getY()-25);
				p3b = Point(p3.getX()+50, p3.getY()+25);
				p3c = Point(p3.getX()+25, p3.getY()+20)
				p3d = Point(p3.getX()-25, p3.getY()-25)
				p4a = Point(p4.getX()-50, p4.getY()-25);
				p4b = Point(p4.getX()+50, p4.getY()+25);
				p4c = Point(p4.getX()+25, p4.getY()+20)
				p4d = Point(p4.getX()-25, p4.getY()-25)
				eye1 = Oval(p3a, p3b);
				eye2 = Oval(p4a, p4b);
				puple = Oval(p3c, p3d)
				puple2= Oval(p4c, p4d)
				eye1.draw(win)
				eye2.draw(win)
				puple.draw(win)
				puple2.draw(win)
				obj.append(puple)
				obj.append(puple2)
				obj.append(eye1)
				obj.append(eye2)

				p6 = win.getMouse()
				p6a = Point(p6.getX()+50,p6.getY())
				p6b = Point(p6.getX()+50,p6.getY()-50)
				nose = Line(p6,p6a);
				nose1= Line(p6,p6b)
				nose.draw(win)
				nose1.draw(win)
				obj.append(nose1)
				obj.append(nose)


				p5 = win.getMouse()
				mouth = Line(Point(p5.getX()+50,p5.getY()), Point(p5.getX()-50,p5.getY()))
				mouth.draw(win)
				obj.append(mouth)
			elif(command[0]=="rect"):
				p1 = win.getMouse();
				p2 = win.getMouse();

				rect = Rectangle(p1,p2);
				length = p1.getX()+p2.getX();
				heidth = p1.getY()+p1.getY();

				area = length*heidth
				prim = 2*(length+heidth)

				print("Primiter: ",prim," Area: ", area)
				rect.draw(win)
				obj.append(rect)
			elif (command[0] =="obj"):
				if(len(command)>=2):
					if(command[1] == "-c"):
						for i in obj:
							i.undraw()
						del obj[:];
				else:
					print(obj)
			else:
				print("Invalid Syntax! Type 'help' for help.");
main();
'''
	[[255, 20], [653, 463]]
'''