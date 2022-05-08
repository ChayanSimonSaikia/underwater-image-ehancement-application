from ImageInfo import ImageInfo


class StoreImage:
    def push(self, img):
        ImageInfo.current_index += 1
        ImageInfo.prev_index = ImageInfo.current_index-1
        ImageInfo.img_dump.append(img)

        print(f"prev: {ImageInfo.prev_index}")
        print(f"current: {ImageInfo.current_index}")
        print(f"next: {ImageInfo.next_index}")

    def undo(self):
        if ImageInfo.current_index == 0:
            return

        ImageInfo.img_bgr = ImageInfo.img_dump[ImageInfo.prev_index]
        if ImageInfo.prev_index != 0:
            ImageInfo.prev_index -= 1

        ImageInfo.current_index -= 1
        ImageInfo.next_index = ImageInfo.current_index + 1
        print(f"prev: {ImageInfo.prev_index}")
        print(f"current: {ImageInfo.current_index}")
        print(f"next: {ImageInfo.next_index}")

    def redo(self):
        if ImageInfo.next_index == 0 or ImageInfo.next_index == len(ImageInfo.img_dump):
            return

        ImageInfo.img_bgr = ImageInfo.img_dump[ImageInfo.next_index]
        ImageInfo.current_index = ImageInfo.next_index - 1
        ImageInfo.prev_index = ImageInfo.current_index - 1
        ImageInfo.next_index += 1

        print(f"prev: {ImageInfo.prev_index}")
        print(f"current: {ImageInfo.current_index}")
        print(f"next: {ImageInfo.next_index}")
