# Here only the logic

proc getAValidValue {min max} {
    set temp [gets stdin]
    while {[expr {![string is integer -strict $temp] || $temp > $max || $temp < $min}]} {
        puts "It's need to be a valid number beetwen $min and $max"
        set temp [gets stdin]
    }
    return $temp
}

proc gen_the_grid {width height prctMine} {
    set grid {}
    for {set i 0} {$i < $height} {incr i} {
        set row {}
        for {set j 0} {$j < $width} {incr j} {
            if {[expr rand()] < $prctMine} {
                lappend row "11"
            } else {
                lappend row "10"
            }
        }
        lappend grid $row
    }
    return $grid
}