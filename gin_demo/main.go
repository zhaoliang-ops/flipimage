package main

import "gin_demo/router"

func main() {

	router := router.StartRouter()
	router.Run(":8001")
}
