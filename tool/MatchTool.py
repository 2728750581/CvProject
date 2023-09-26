#opencv模板匹配----单目标匹配
import cv2

def ImageMatch(target, template):
    #获得模板图片的高宽尺寸
    theight, twidth = template.shape[:2]
    #执行模板匹配，采用的匹配方式cv2.TM_SQDIFF_NORMED
    result = cv2.matchTemplate(target, template, cv2.TM_SQDIFF_NORMED)
    #归一化处理
    cv2.normalize(result, result, 0, 1, cv2.NORM_MINMAX, -1)
    #寻找矩阵（一维数组当做向量，用Mat定义）中的最大值和最小值的匹配结果及其位置
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    return min_loc, twidth, theight, min_val

if __name__=='__main__':
    target = cv2.imread("bin\\scene.png")
    template = cv2.imread("bin\\shotcut.png")
    min_loc, twidth, theight, val = ImageMatch(target, template)

    cv2.rectangle(target, min_loc,
                (min_loc[0]+twidth, min_loc[1]+theight), (0, 0, 225), 2)
    #显示结果,并将匹配值显示在标题栏上
    cv2.imshow("MatchResult----MatchingValue", target)
    cv2.imwrite('bin\\result.png', target)
    cv2.waitKey()
    cv2.destroyAllWindows()

