from ImageInfo import ImageInfo


class UndoStack:
    def push(self, img):
        if ImageInfo.prev_index == None:
            ImageInfo.prev_index = 0
        else:
            ImageInfo.prev_index += 1

        ImageInfo.img_dump.append(img)

    def undo(self):
        if ImageInfo.prev_index == None:
            return
        if ImageInfo.prev_index <= 0:
            ImageInfo.img_bgr = ImageInfo.img_bgr_original
            ImageInfo.img_dump = []
            return

        ImageInfo.img_bgr = ImageInfo.img_dump[ImageInfo.prev_index-1]

        if ImageInfo.prev_index != 0:
            ImageInfo.prev_index -= 1
            return

        ImageInfo.prev_index = None
        ImageInfo.img_dump.pop()
