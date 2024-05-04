package main

import (
	"fmt"
	"strconv"
)

func main() {
	bruteForce()
	DevideNConquer()

}

func bruteForce() {
	var password string
	var status bool
	fmt.Print("Input your password: ")
	fmt.Scan(&password)

	for guess := 0; guess < 10000 && !status; guess++ {

		guessString := makeIt4digits(guess)

		fmt.Printf("Your guess: '%v'\n", guessString)
		if guessString != password {
			fmt.Println("Access Denied")
		} else {
			fmt.Println("Access Granted")
			status = true
		}
	}
}

func makeIt4digits(n int) string {
	//convert integer into string
	nString := strconv.Itoa(n)

	//add the number 0 to make the data, 4 digits
	if len(nString) == 1 {
		nString = "0" + "0" + "0" + nString
	} else if len(nString) == 2 {
		nString = "0" + "0" + nString
	} else if len(nString) == 3 {
		nString = "0" + nString
	}
	return nString
}

func DevideNConquer() {
	var listProbInt []int
	var password string

	//input password
	fmt.Print("Input your password: ")
	fmt.Scan(&password)

	//convert the password into int
	intPassword, _ := strconv.Atoi(password)

	for i := 0; i < 10000; i++ {
		//inset the possibility into the slice
		listProbInt = append(listProbInt, i)
	}

	//use binary search to find the correct password
	left := 0
	right := len(listProbInt) - 1
	mid := (left + right) / 2

	for listProbInt[mid] != intPassword && left != right {
		fmt.Println("Your guess: ", listProbInt[mid])
		if intPassword > listProbInt[mid] {
			left = mid + 1
			fmt.Println("Access Denied (Terlalu kecil)")
		} else {
			right = mid - 1
			fmt.Println("Access Denied (Terlalu besar)")
		}
		mid = (left + right) / 2
	}
	fmt.Println("Your guess: ", listProbInt[mid])
	fmt.Println("Access Granted")
}
