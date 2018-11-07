
def test(request):
    current_user = request.user
    print(current_user.id)