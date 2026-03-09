# Not finished yet

# Warning you need to be in the right folder otherwise the import will not work 
#(path relative to the pwd and not tothe file)

source logic.tcl
source colorize.tcl
source keyboard.tcl

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
    puts -nonewline "\033\c"
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


enableRaw
while 1 {
        set k [readkey]
        if {$k == "q" || $k == "Q"} break
        if {$k == "DOWN" && [lindex $cursor 0] < ($height - 1)} {
            lset cursor 0 [expr [lindex $cursor 0] + 1]
            print "standar"
        }
        if {$k == "UP" && [lindex $cursor 0] > 0} {
            lset cursor 0 [expr [lindex $cursor 0] - 1]
            print "standar"
        }
        if {$k == "RIGHT" && [lindex $cursor 1] < ($width - 1)} {
            lset cursor 1 [expr [lindex $cursor 1] + 1]
            print "standar"
        }
        if {$k == "LEFT" && [lindex $cursor 1] > 0} {
            lset cursor 1 [expr [lindex $cursor 1] - 1]
            print "standar"
        }
        if {$k == "SPACE"} {
            set grid [flagIt $grid [lindex $cursor 0] [lindex $cursor 1]]
            print "standar"
        }
        #puts "$cursor "
}
disableRaw