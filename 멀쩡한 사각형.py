#멀쩡한 사각형
def solution(w,h):
    if w==h:
        return (w*h) - w
    else:
        return w*h - solution(h, w%h)