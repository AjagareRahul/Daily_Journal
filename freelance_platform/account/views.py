from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponseForbidden
from .models import Profile
from .forms import ProfileForm
from django.contrib.auth.decorators import login_required

# Display all profiles on the home page
def home(request):
    # Fetch all Profile objects from the database
    profile=Profile.objects.all()
    # Render the home template with all profiles
    return render(request,'home.html',{'profile':profile})

# Create a new profile for the logged-in user
@login_required
def create_profile(request):
    # Check if user already has a profile - redirect to update instead
    if Profile.objects.filter(user=request.user).exists():
        user_profile = Profile.objects.get(user=request.user)
        return redirect('update_profile', id=user_profile.id)
    
    # Handle form submission
    if request.method=='POST':
        # Bind form to POST data
        form=ProfileForm(request.POST)
        # Validate form data
        if form.is_valid():
            # Save but don't commit yet to add user
            profile=form.save(commit=False)
            # Associate profile with current logged-in user
            profile.user=request.user
            # Save the profile to database
            profile.save()
            # Redirect to home page after successful creation
            return redirect('home')
    else:
        # Show empty form for GET request
        form=ProfileForm()
    
    # Render create profile template with form
    return render(request,'create_profile.html',{'form':form})

# Update an existing profile (only the owner should be able to update)
@login_required
def update_profile(request, id):
    # Get profile by id or return 404 if not found
    profile = get_object_or_404(Profile, id=id)
    
    # Authorization check: only the profile owner can update
    if profile.user != request.user:
        return HttpResponseForbidden("You can only update your own profile.")

    # Handle form submission
    if request.method == 'POST':
        # Bind form to POST data and existing profile instance
        form = ProfileForm(request.POST, instance=profile)
        # Validate form data
        if form.is_valid():
            # Save updates directly (user field remains unchanged)
            form.save()
            # Redirect to home page after successful update
            return redirect('home')
    else:
        # Show form pre-filled with existing profile data
        form = ProfileForm(instance=profile)

    # Render update profile template with form
    return render(request, 'update_profile.html', {'form': form})

# View to let logged-in user access their own profile update page
@login_required
def my_profile(request):
    # Try to get user's profile, redirect to create if not exists
    try:
        user_profile = Profile.objects.get(user=request.user)
        return redirect('update_profile', id=user_profile.id)
    except Profile.DoesNotExist:
        return redirect('create_profile')
    