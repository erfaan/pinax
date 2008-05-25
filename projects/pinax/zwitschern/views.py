from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required

# from django.contrib.auth.models import User

from zwitschern.models import Tweet, TweetInstance, tweet

@login_required
def personal(request):
    """
    just the tweets the current user is following
    """
    if request.method == "POST":
        if request.POST["action"] == "post":
            text = request.POST["tweet"].strip()
            tweet(request.user, text)
    
    tweets = TweetInstance.objects.filter(recipient=request.user).order_by("-sent")
    
    return render_to_response("zwitschern/personal.html", {
        "tweets": tweets,
    }, context_instance=RequestContext(request))

def public(request):
    """
    all the tweets
    """
    tweets = Tweet.objects.all().order_by("-sent")

    return render_to_response("zwitschern/public.html", {
        "tweets": tweets,
    }, context_instance=RequestContext(request))