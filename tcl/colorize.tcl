# This is the file of the colorize function

proc colorize {nb i j type cursor} {
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
    switch $nb {
        "1" {
            set nbColor "\u001b\[38;2;73;74;210m\u001b\[1m"
        }
        "2" {
            set nbColor "\u001b\[38;2;64;120;67m\u001b\[1m"
        }
        "3" {
            set nbColor "\u001b\[38;2;210;73;73m\u001b\[1m"
        }
        "4" {
            set nbColor "\u001b\[38;2;140;57;161m\u001b\[1m"
        }
        "5" {
            set nbColor "\u001b\[38;2;243;237;38m\u001b\[1m"
        }
        "6" {
            set nbColor "\u001b\[38;2;106;232;226m\u001b\[1m"
        }
        "7" {
            set nbColor "\u001b\[38;2;133;133;131m\u001b\[1m"
        }
        default {
            set nbColor "\u001b\[38;2;0;0;0m\u001b\[1m"
        }
    }
    #if cusor here
    if {([lindex $cursor 0] == $i) && ([lindex $cursor 1] == $j) && !($type eq "win")} {
        if {($nb == 11) && ($type eq "loose")} {
            return "$mine_color\[X\]$clear"
        } elseif {($nb >= 12) && !($type eq "win")} {
            return "$green\[${flag_color}F$clear$green\]$clear"
        } elseif {$nb >= 10} {
            return "$green\[ \]$clear"
        } elseif {$nb == 0} {
            return "$brown\[ \]$clear"
        } else {
            return "$brown\[$nbColor$nb$clear$brown\]$clear"
        }
    }

    if {($nb == 11) && ($type eq "loose")} {
        return "$mine_color X $clear"
    } elseif {($nb == 13) && ($type eq "loose")} {
        return "$mine_color F $clear"
    } elseif {($nb >= 12) && !($type eq "win")} {
        return "$green$flag_color F $clear"
    } elseif {$nb >= 10} {
        return "$green   $clear"
    } elseif {($nb == 0) && !($type eq "win")} {
        return "$brown   $clear"
    } elseif {$type eq "win"} {
        return "$blue   $clear"
    } else {
        return "$brown$nbColor $nb $clear"
    }
}