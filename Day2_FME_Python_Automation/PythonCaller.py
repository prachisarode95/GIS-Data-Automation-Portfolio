def fme_feature(feature):
    area = float(feature.getAttribute('area'))
    if area > 2000:
        category = 'Large'
    elif area > 1000:
        category = 'Medium'
    else:
        category = 'Small'

    feature.setAttribute('category', category)
    feature.setAttribute('tag', 'FME+Python')