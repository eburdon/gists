package main

import (
	"fmt"
)

func pointers() {
	b := 255
	var a *int = &b
	fmt.Printf("Type of a is %T\n", a)
	
	fmt.Println("value of b is", b)
	fmt.Println("address of b is", a)
	
	fmt.Println("value of b [2] is", *a)
}

func main() {
	pointers()
}
