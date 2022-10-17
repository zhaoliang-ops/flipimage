package router

import (
	api "gin_demo/controller/api"

	"github.com/gin-gonic/gin"
)

func StartRouter() *gin.Engine {
	router := gin.Default()
	router.GET("/api/publish", api.Publish)
	router.GET("/api/consumer", api.Consumer)
	return router
}
