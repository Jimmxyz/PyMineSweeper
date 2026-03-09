proc enableRaw {{channel stdin}} {
   exec /bin/stty raw -echo <@$channel
}
proc disableRaw {{channel stdin}} {
   exec /bin/stty -raw echo <@$channel
}

proc put {str} {puts -nonewline $str; flush stdout}

# read char from stdin
proc readchar {} {
        return [read stdin 1]
}

# This is a complete detection key program you can use
# come from : https://wiki.tcl-lang.org/page/Reading+a+single+character+from+the+keyboard+using+Tcl
proc readkey {} {
        set c [readchar]
        set d [scan $c %c]
        switch $d {
                9   {return TAB}
                10  {return ENTER}
                32  {return SPACE}
                127 {return BACKSPACE}
                27  {
                        set c [readchar]
                        switch $c {
                                \[ {
                                        set c [readchar]
                                        switch $c {
                                                A {return UP}
                                                B {return DOWN}
                                                C {return RIGHT}
                                                D {return LEFT}
                                                F {return HOME}
                                                H {return HOME}
                                                P {return PAUSE}
                                                1 {
                                                        set c [readchar]
                                                        switch $c {
                                                                5 {if {[readchar]=="~"} {return F5}}
                                                                7 {if {[readchar]=="~"} {return F6}}
                                                                8 {if {[readchar]=="~"} {return F7}}
                                                                9 {if {[readchar]=="~"} {return F8}}
                                                                ~ {return HOME}
                                                        }
                                                }
                                                2 {
                                                        set c [readchar]
                                                        switch $c {
                                                                0 {if {[readchar]=="~"} {return F9}}
                                                                1 {if {[readchar]=="~"} {return F10}}
                                                                3 {if {[readchar]=="~"} {return F11}}
                                                                4 {if {[readchar]=="~"} {return F12}}
                                                                ~ {return INSERT}
                                                        }
                                                }
                                                3 {if {[readchar]=="~"} {return DELETE}}
                                                4 {if {[readchar]=="~"} {return END}}
                                                5 {if {[readchar]=="~"} {return PAGEUP}}
                                                6 {if {[readchar]=="~"} {return PAGEDOWN}}
                                                default {return $c}
                                        }
                                }
                                O {
                                        set c [readchar]
                                        switch $c {
                                                P {return F1}
                                                Q {return F2}
                                                R {return F3}
                                                S {return F4}
                                                default {return $c}
                                        }
                                }
                                default {
                                        set d [scan $c %c]
                                        if {$d < 32} {
                                                set d [expr {$d + 64}]
                                                set c [format %c $d]
                                                return CTRL+ALT+$c
                                        }
                                        set c [string toupper $c]
                                        return ALT+$c
                                }
                        }
                }
                default {
                        if {$d < 32} {
                                set k [expr {$d + 64}]
                                set c [format %c $k]
                                return CTRL-$c
                        } else {
                                return [format %c $d]
                        }
                }
        }
}