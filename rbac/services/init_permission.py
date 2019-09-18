from luffy_permission import settings


def init_permissions(curent_user, request):
    """
     用户权限初始化
    :param curent_user:   当前用户对象
    :param request:  请求相关所有数据
    :return:
    """
    # 2  用户权限初始化
    # 根据当前用户信息获取此用户所拥有的的所有权限  并放入到session中
    # 当前用户所有权限
    permission_queryest = curent_user.roles.filter(permissions__isnull=False).values('permissions__id',
                                                                                     'permissions__title',
                                                                                     'permissions__url',
                                                                                     'permissions__name',
                                                                                     'permissions__pid_id',
                                                                                     'permissions__pid__title',
                                                                                     'permissions__pid__url',
                                                                                     'permissions__menu_id',
                                                                                     'permissions__menu__title',
                                                                                     'permissions__menu__icon',
                                                                                     ).distinct()
    # permission_list = curent_user.roles.all().values('permissions__id', 'permissions__url').distinct()
    # print(permission_list)

    #  获取权限菜单信息
    # 获取权限中所有的URL
    # permissions_list = []
    # for item in permission_queryest:
    #     permissions_list.append(item['permissions__url'])
    #     # print(item)
    #     print(permissions_list)
    # print('______')

    # 3  获取权限 菜单信息
    # permission_list = []
    permission_dict = {}

    menu_dict = {}

    for item in permission_queryest:
        # permission_list.append({
        #     'id': item['permissions__id'],
        #     'url': item['permissions__url'],
        #     'title': item['permissions__title'],
        #     'pid': item['permissions__pid_id'],
        #     'p_title': item['permissions__pid__title'],
        #     'p_url': item['permissions__pid__url'],
        # })
        permission_dict[item['permissions__name']] = {
            'id': item['permissions__id'],
            'url': item['permissions__url'],
            'title': item['permissions__title'],
            'pid': item['permissions__pid_id'],
            'p_title': item['permissions__pid__title'],
            'p_url': item['permissions__pid__url'],
        }

        # permission_list.append(item['permissions__url'])
        menu_id = item['permissions__menu_id']
        if not menu_id:
            continue
        node = {'id': item['permissions__id'], 'title': item['permissions__title'], 'url': item['permissions__url']}
        if menu_id in menu_dict:
            menu_dict[menu_id]['children'].append(node)
        else:
            menu_dict[menu_id] = {
                'title': item['permissions__menu__title'],
                'icon': item['permissions__menu__icon'],
                'children': [node, ]
            }

    # permission_list = [item['permissions__url'] for item in permission_queryest]

    # print(permission_list)
    # print(menu_dict)

    request.session[settings.PERMISSION_SISSION_KEY] = permission_dict
    request.session[settings.MENU_SISSION_KEY] = menu_dict
