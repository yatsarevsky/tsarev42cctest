from django.shortcuts import render_to_response, redirect
from django.template.context import RequestContext
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

from yaproject.vcard.models import VCard, RequestStore
from yaproject.vcard.forms import MemberAccountForm, VCardForm


def contacts(request):
    contacts = VCard.objects.get(pk=1)
    return render_to_response('vcard/vcard_detail.html',
        {'contacts': contacts}, RequestContext(request))


def requests_store(request):
    requests = RequestStore.objects.all().order_by('id')[:10]
    return render_to_response('requests.html',
        {'requests': requests}, RequestContext(request))
<<<<<<< HEAD
=======


@login_required(login_url='/login/')
def edit_page(request):
    instance = VCard.objects.get(pk=1)
    form = VCardForm(instance=instance)

    if request.POST:
        form = VCardForm(request.POST, request.FILES, instance=instance)

        if form.is_valid():
            form.save()
            return redirect('home')

    return render_to_response('vcard/edit_vcard.html',
        {'form': form}, RequestContext(request))


def accounts_registration(request):
    form = MemberAccountForm()

    if request.POST:
        form = MemberAccountForm(request.POST)

        if form.is_valid():
            form.save(commit=False)
            password = form.cleaned_data['password']
            user = User.objects.create_user(email=form.cleaned_data['email'],
                username=form.cleaned_data['username'],
                password=password)
            user.is_active = True
            user.set_password(password)
            user.is_authenticated()
            user.save()
            user = authenticate(username=user.username, password=password)
            login(request, user)
            return redirect('home')

    return render_to_response('accounts/signup_member.html',
        {'form': form}, RequestContext(request))


def logout_account(request):
    logout(request)
    return HttpResponseRedirect(reverse("home"))
>>>>>>> master
