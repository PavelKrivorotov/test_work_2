from collections import namedtuple

from django.db import connection


class MenuManager:
    def __init__(self, menu_name, menu_item=None) -> None:
        self.menu_name = menu_name
        self.menu_item = menu_item

        self.rows = self.raw_sql_query()

    def raw_sql_query(self):
        query = """
            SELECT
                menu_menuitem.id,
                menu_menuitem.title,
                menu_menuitem.root,

                menu_menurelation.children_id
            FROM
                menu_menuitem
            LEFT JOIN
                menu_menurelation
            ON
                menu_menuitem.id = menu_menurelation.item_id
        """

        with connection.cursor() as cursor:
            cursor.execute(query)
            return self._to_namedtuple(cursor)

    def show(self):
        root = self._get_root_id()
        items = self._get_childrens(root.id)
        return [(item, 1) for item in items]

    def open(self):
        root = self._get_root_id()
        items = self.recursive_menu(root)
        return items
    
    def _to_namedtuple(self, cursor):
        nt_result = namedtuple(
            'Row',
            [col[0] for col in cursor.description]
        )
        return [nt_result(*row) for row in cursor.fetchall()]

    def _get_root_id(self):
        for obj in self.rows:
            if obj.title == self.menu_name:
                return obj

    def _get_childrens(self, id):
        inds = [obj.children_id for obj in self.rows if obj.id == id and obj.children_id is not None]

        objs = []
        inds_tmp = []
        for obj in self.rows:
            for ind in sorted(inds):
                if obj.id == ind and obj.id not in inds_tmp:
                    objs.append(obj)
                    inds_tmp.append(obj.id)
        return objs

    def recursive_menu(self, obj):
        result = list()
        flag = False

        def _recursive_menu(obj, result, depth=0, depth_parent=0):
            nonlocal flag

            # OKEY -> worked
            # if flag:
            #     if (depth - depth_parent) > 2:
            #         return result

            if not obj.root:
                result.append((obj, depth))

            # worked too!
            if flag:
                if (depth - depth_parent) > 1:
                    return result

            children = self._get_childrens(obj.id)
            for child in children:
                if child.id == self.menu_item:
                    flag = True
                    depth_parent = depth

                if flag:
                    result = _recursive_menu(child, result, depth + 1, depth_parent)
                else:
                    result = _recursive_menu(child, result, depth + 1, depth)

            return result
        return _recursive_menu(obj, result)

