# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 20:20:13 2020

@author: user
"""

class Shape:
    # -- Class Vars
    name = "Shape"


    # --
    # -- The ToString function for this class - it is what is called when you print( str( shape ) )
    # -- Note: You need to use str( x ) to convert that object to a string - most data-types have an appropriate To-String function to do this and if not you'll be left with something like <address / reference / other info>
    # --
    def __str__( self ):
        return "I am a " + self.name + " defined as " + type( self ).__name__ + "( ... )"


# --
# -- Square extends Shape - A Square has the same width / height so we only need 1 value, we'll use X but it can be anything we want..
# --
class Square( Shape ):
    # -- Class Vars
    name = "Square"

    # -- Set x to a default value
    x = 0


    # --
    # -- Object Creation - We'll use this to create a square: Square( 10 ) for example.
    # --
    def __init__( self, _x ):
        # -- Run the BaseClass - Although Shape doesn't do anything, it's here to fall all the way through just in case...
        super( ).__init__( )

        # -- We can set the name here, or just leave it in the class - Note: The same can be done in Rect but I omitted it to keep this example short...
        # -- self.name = "Square"

        # -- Update X for this instance - Note: I'd typically use a Getter / Setter for all variables to prevent incorrect data-types or usage
        self.x = _x


    # --
    # -- The ToString function for this class - it is what is called when you print( str( shape ) )
    # -- Note: You need to use str( x ) to convert that object to a string - most data-types have an appropriate To-String function to do this and if not you'll be left with something like <address / reference / other info>
    # --
    def __str__( self ):
        return "I am a " + self.name + " defined as " + type( self ).__name__ + "( " + str( self.x ) + " ) ie x = " + str( self.x ) + " with an area of " + str( self.area( ) )


    # --
    # --
    # --
    def area( self ):
        return self.x * self.x


# --
# -- Cube extends Shape - This cube is coded to change a few of the functions from Square - it is also coded as a 1 var shape, ie all sides are the same..
# --
class Cube( Square ):
    # -- Class Vars
    name = "Cube"


    # --
    # -- Object Creation - We'll use this to create a square: Square( 10 ) for example.
    # --
    def __init__( self, _x ):
        # -- Run the BaseClass - Although Shape doesn't do anything, it's here to fall all the way through just in case...
        super( ).__init__( _x )


    # --
    # -- The ToString function for this class - it is what is called when you print( str( shape ) )
    # -- Note: You need to use str( x ) to convert that object to a string - most data-types have an appropriate To-String function to do this and if not you'll be left with something like <address / reference / other info>
    # --
    def __str__( self ):
        return super( ).__str__( ) + " with an area of " + str( self.area( ) )


    # --
    # --
    # --
    def area( self ):
        return self.x ** self.x


# --
# -- Rectangle extends Square extends Shape ( Same as class Rect( Square, Shape ) but Square extends Shape so it shouldn't be needed for fallthrough )
# -- A Rectangle has different width and height so we'll use x from square for width, and add y for height to make a rectangle...
# --
class Rect( Square ):
    # -- Class Vars
    name = "Rectangle"

    # -- Set y to a default value so we don't need to worry about errors if it isn't defined
    y = 0


    # --
    # -- Object Creation - We'll use this to create a rectangle: Rect( 10, 20 ) for example.
    # --
    def __init__( self, _x, _y ):
        # -- Run the BaseClass - This is needed to set self.x by allowing Square to execute that - we could also do self.x = x, but this is an example of inheritance so...
        super( ).__init__( _x )

        # -- Update y for this instance - Note: I'd typically use a Getter / Setter for all variables to prevent incorrect data-types or usage - but to keep things short, I kept things simple...
        self.y = _y


    # --
    # -- The ToString function for this class - it is what is called when you print( str( shape ) )
    # -- Note: You need to use str( x ) to convert that object to a string - most data-types have an appropriate To-String function to do this and if not you'll be left with something like <address / reference / other info>
    # --
    def __str__( self ):
        return "I am a " + self.name + " defined as " + type( self ).__name__ + "( " + str( self.x ) + ", " + str( self.y ) + " ) ie x = " + str( self.x ) + " / y = " + str( self.y ) + " with an area of " + str( self.area( ) )


    # --
    # --
    # --
    def area( self ):
        return self.x * self.y


# --
# -- Main
# --
def main( ):
    # -- Create a rectangle with x = 10, y = 20
    _shape = Rect( 10, 20 )

    # -- Create a rectangle with x = 30, y = 40
    _shape2 = Rect( 30, 40 )

    # -- Create a square with x = 50
    _shape3 = Square( 50 )

    # -- Create a simple Shape - with nothing attached...
    _shape4 = Shape( )

    # -- Create a simple Cube...
    _shape5 = Cube( 4 )

    # --
    # -- I'm doing the output text here so you know that declaring other shapes won't overwrite other values in other objects
    # -- if I were set up the output text after each object creation and allow another object to be created afterwards
    # --    it wouldn't prove that the objects have their own values meaning it would be possible for the variables to be
    # --    static ( shared among all types so the last object to update that value would mean all objects have that value )
    # --    but, by having all text here, it shows that the variables aren't static - they're private..
    # --
    # -- Note: I left the original outputs commented to the right of the new str( object ) method so you could see one way of doing it vs the benefits of having a __str__ ToString method handle it for you...
    # --

    # Define the text output var... Then add to it for each line...
    _text = ""

    # -- This is calling Rect ToString function normally
    # -- Originals output without using tostring method -- # _text += _shape.name + " x: " + str( _shape.x ) + " y: " + str( _shape.y ) + "\n"
    _text += str( _shape ) + "\n"

    # -- This is calling Square ToString function ( ie super of Rect is Square ) -- Output: I am a Rectangle defined as Rect( 10 ) ie x = 10
    _text += str( super( Rect, _shape ).__str__( ) ) + "\n"

    # -- This is calling Shape ToString function ( ie super of Square is Shape ) -- Output: I am a Rectangle defined as Rect( ... )
    _text += str( super( Square, _shape ).__str__( ) ) + "\n"

    # -- This calls Rect ToString function normally
    # -- Originals output without using tostring method -- # _text += _shape2.name + " x: " + str( _shape2.x ) + " y: " + str( _shape2.y ) + "\n"
    _text += str( _shape2 ) + "\n"

    # -- This calls Square ToString function normally
    # -- Originals output without using tostring method -- # _text += _shape3.name + " x: " + str( _shape3.x ) + "\n"
    _text += str( _shape3 ) + "\n"

    # -- This calls Shape ToString function normally
    _text += str( _shape4 ) + "\n"

    # -- This calls Shape ToString function normally
    _text += str( _shape5 ) + "\n"

    # -- Output:
    # I am a Rectangle defined as Rect( 10, 20 ) ie x = 10 / y = 20 with an area of 200
    # I am a Rectangle defined as Rect( 10 ) ie x = 10 with an area of 200
    # I am a Rectangle defined as Rect( ... )
    # I am a Rectangle defined as Rect( 30, 40 ) ie x = 30 / y = 40 with an area of 1200
    # I am a Square defined as Square( 50 ) ie x = 50 with an area of 2500
    # I am a Shape defined as Shape( ... )
    # I am a Cube defined as Cube( 4 ) ie x = 4 with an area of 256 with an area of 256
    return _text


# --
# -- Call main and print the return contents...
# --
print( main( ) )