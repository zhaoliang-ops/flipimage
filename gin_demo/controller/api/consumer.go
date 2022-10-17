package api

import (
	lib "gin_demo/utils"

	"github.com/gin-gonic/gin"
)

func Consumer(*gin.Context) {
	rabbitmq := lib.NewRabbitMQSimple("fliped_images")
	rabbitmq.ConsumeSimple()
}
