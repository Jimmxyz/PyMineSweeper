# Not finished yet

# Warning you need to be in the right folder otherwise the import will not work 
#(path relative to the pwd and not tothe file)

source logic.tcl
source colorize.tcl

puts "Choose the width of the grid : "
set width [getAValidValue 5 30]
puts "Choose the height of the grid : "
set height [getAValidValue 5 30]
puts "Choose the percentage of mine : "
set prct [expr [getAValidValue 4 96] / 100.0]
#puts $prct

set grid [gen_the_grid $width $height $prct]
#puts $grid

set cursor {0 0}

proc print {type} {
    global grid cursor
    set i_index 0
    foreach i $grid {
        set j_index 0
        foreach j $i {
            puts -nonewline [colorize $j $i_index $j_index $type $cursor]
            incr j_index
        }
        puts ""
        incr i_index
    }

}

print "standar"