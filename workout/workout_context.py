def user_context(request):
    context = {'user': request.user}
    return context
