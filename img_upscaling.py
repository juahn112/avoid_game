def upscaling_image(file_path):
    import cv2
    from cv2 import dnn_superres

    sr = dnn_superres.DnnSuperResImpl_create()

    model_path = "EDSR_x4.pb"
    target_img = cv2.imread(file_path)
    sr.readModel(model_path)
    sr.setModel("edsr", 4)

    upscaled_img = sr.upsample(target_img)
    cv2.imwrite('img/upscaling_image2.png', upscaled_img)

upscaling_image("img/upscaling_image.png")

