import string

class Tile():
    def __init__(self):
        self.coord_x = 0
        self.coord_y = 0
        self.tile_contents = "water"
        self.is_hit = False

    def __repr__(self):
        if self.tile_contents == "ship":
            if self.is_hit:
                return "[*]"
            else:
                return "[ ]"
        if self.tile_contents == "water":
            if self.is_hit:
                return " * "   
            else:
                return " . "

    def do_hit(self):
        self.is_hit = True
        return self.tile_contents
        
    def set_type(self, tile_type):
        self.tile_contents = tile_type
        
    

class Field():
    
    def __init__(self, rows = 10, cols = 10):
        local_grid = []

        while len(local_grid) < rows:
            local_col = []
            while len(local_col) < cols:
                local_col.append(Tile())
            
            local_grid.append(local_col)

        self.grid = local_grid

    def __repr__(self):
        repr_string = ''
        current_col_index = 0
        indicies = list(' ' + string.ascii_lowercase)
        while current_col_index <= len(self.grid):
            repr_string += " {} ".format(indicies[current_col_index])
            current_col_index += 1
        repr_string += "\n"

        row_index = 0
        for row in self.grid:
            row_index += 1
            if row_index < 10:
                repr_string += " {} ".format(str(row_index))
            else:
                repr_string += "{} ".format(str(row_index))
            
            for col in row:
                repr_string += repr(col)
            repr_string += "\n"

        return repr_string

    def place_ship(self, rowcol, direction, length):
        """
        This function returns True, if it was able to place a ship, False otherwise
        It should fill tiles (see Tile class) with corresponding type.

        For your convenience, row_index and col_index are already mapped to correct values of indicies
        in grid - as list starts with index 0
        """

        row_index = int(rowcol[1:])-1
        col_index = string.ascii_lowercase.index(rowcol[0])

        if (direction == "right") and (col_index <= len(self.grid[0]) - length) :
             for i in range(length):
              field.grid[row_index][col_index+i].set_type("ship")
        elif (direction == "right") and (col_index > len(self.grid[0]) - length):
            return False

        if (direction == "down") and (row_index <= len(self.grid[0]) - length) :
            for i in range(length):
                field.grid[row_index+i][col_index].set_type("ship")
        elif (direction == "down") and (row_index > len(self.grid[0]) - length):
            return False
    

        
        
            
        



field = Field()

if field.place_ship("e9", "down", 3):
    print "Ship placed sucessfully"
else:
    print "Ship palacement failed"


print field
