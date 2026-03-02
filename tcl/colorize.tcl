# This is the file of the colorize function

proc colorize {nb i j type} {
    # init var
    set clear "\u001b\[0m"
    set blue "\u001b\[48;2;26;122;201m"
    set mine_color "\u001b\[48;2;201;75;26m\u001b\[1m"

    # Background for normal / win / lose states
    if {(($i + $j) % 2 == 0) && ($type eq "standar" || $type eq "win")} {
        set green "\u001b\[48;2;88;168;88m"
        set brown "\u001b\[48;2;231;164;133m"
    } elseif {$type eq "standar" || $type eq "win"} {
        set green "\u001b\[48;2;82;153;82m"
        set brown "\u001b\[48;2;214;140;105m"
    }
    # Loose here

    set flag_color "\u001b\[38;2;210;0;0m\u001b\[1m"

    #color nb here

    #if cusor here

    if {($nb == 11) && ($type eq "loose")} {
        # here
    } elseif {($nb == 13) && ($type eq "loose")} {
        # here
    } elseif {($nb >= 12) && !($type eq "win")} {
        # here
    } elseif {$nb >= 10} {
        return "$green   $clear"
    }
}