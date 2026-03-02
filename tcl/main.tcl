# Not finished yet

source logic.tcl

puts "Choose the width of the grid : "
set width [getAValidValue 5 30]
puts "Choose the height of the grid : "
set height [getAValidValue 5 30]
puts "Choose the percentage of mine : "
set prct [expr [getAValidValue 4 96] / 100.0]
#puts $prct

set grid [gen_the_grid $width $height $prct]
#puts $grid