package api

import (
	"fmt"
	"gin_demo/controller/image"
	lib "gin_demo/utils"

	"github.com/gin-gonic/gin"
)

func Publish(c *gin.Context) {

	path := c.Query("orginal_images")
	// fmt.Println("路径:" + path)
	readImage := new(image.ReadImage)
	if err := readImage.ReadAllImages(path); err != nil {
		fmt.Println(err.Error())
	} else {
		fmt.Println(readImage.FilesName)
	}
	// 开启协程 多实例推送mq
	go func() {
		for d := range readImage.FilesName {
			// 实现我们要实现的逻辑函数
			rabbitmq := lib.NewRabbitMQSimple("flip_images")
			// fmt.Println("发送:" + readImage.FilesName[d])
			rabbitmq.PublishSimple(readImage.FilesName[d])
		}
	}()
}
