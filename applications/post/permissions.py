from rest_framework.permissions import BasePermission, SAFE_METHODS

# GET POST GET id PUt ID DELETE ID 
class IsOwnerOrAdminOrReadOnly(BasePermission):
    
    # def has_permission(self, request, view):
    #     return request.user.is_authenticated
    
    def has_object_permission(self, request, view, obj):
        # print(request.method)
        # print(SAFE_METHODS)
        # if request.metod in SAFE_METHODS:
        #     ...
        if request.method == 'GET':
            return request.user.is_authenticated
        return request.user.is_authenticated and request.user == obj.owner or request.user.is_staff
# True and admin@admin == admin@admin