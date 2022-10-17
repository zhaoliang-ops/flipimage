package image

import (
	"errors"
	"io/ioutil"
	"os"
	"regexp"
)

type ReadImage struct {
	FilesName []string
	FilesInfo []os.FileInfo
}

func (r *ReadImage) ReadAllImages(path string) (err error) {

	if r.FilesInfo, err = ioutil.ReadDir(path); err != nil {
		err = errors.New("读取文件失败: " + path)
		return
	}
	var reg = regexp.MustCompile(`.\.{1}jpg$`)
	for _, fileInfo := range r.FilesInfo {
		if fileInfo.IsDir() {
			r.ReadAllImages(path + "/" + fileInfo.Name())
		} else {
			if reg.MatchString(fileInfo.Name()) {
				r.FilesName = append(r.FilesName, path+"/"+fileInfo.Name())
			}
		}
	}

	return
}
