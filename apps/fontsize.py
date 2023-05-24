def fontsize(base_fontsize, target_fontsize, lineheight):
    lineheight_px = base_fontsize * lineheight
    target_lineheight = lineheight_px / target_fontsize
    target_fontsize_em = 1.0 / base_fontsize * target_fontsize
    target_lineheight = round(target_lineheight, 4)
    target_fontsize_em = round(target_fontsize_em, 4)
    return "###################\nfont-size: %sem\nline-height: %s\nmargin-bottom: %s\n###################" % (target_fontsize_em, target_lineheight, target_lineheight)


