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
        else:
            ImageInfo.img_bgr = ImageInfo.img_dump[ImageInfo.prev_index-1]

        if ImageInfo.prev_index != 0:
            ImageInfo.prev_index -= 1
            ImageInfo.next_index = ImageInfo.prev_index + 1
        else:
            ImageInfo.prev_index = None
            ImageInfo.next_index = 0

    def redo(self):
        if ImageInfo.next_index == None:
            return
        if ImageInfo.next_index == len(ImageInfo.img_dump):
            ImageInfo.next_index = None
            return

        ImageInfo.img_bgr = ImageInfo.img_dump[ImageInfo.next_index]
        ImageInfo.prev_index = ImageInfo.next_index
        ImageInfo.next_index += 1
