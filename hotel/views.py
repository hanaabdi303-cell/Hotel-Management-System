from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Room, RoomCategory, Customer, Reservation

# --- DASHBOARD VIEW ---
@login_required
def dashboard(request):
    context = {
        'total_rooms': Room.objects.count(),
        'available_rooms': Room.objects.filter(status='Available').count(),
        'total_customers': Customer.objects.count(),
        'active_reservations': Reservation.objects.exclude(status='Checked-Out').count(),
    }
    return render(request, 'hotel/dashboard.html', context)

# --- CATEGORY MANAGEMENT VIEWS ---
@login_required
def category_list(request):
    categories = RoomCategory.objects.all()
    return render(request, 'hotel/category_list.html', {'categories': categories})

@login_required
def category_add(request):
    if request.method == 'POST':
        RoomCategory.objects.create(
            name=request.POST.get('name'),
            description=request.POST.get('description')
        )
        return redirect('category_list')
    return render(request, 'hotel/category_form.html')

@login_required
def category_edit(request, id):
    category = get_object_or_404(RoomCategory, id=id)
    if request.method == 'POST':
        category.name = request.POST.get('name')
        category.description = request.POST.get('description')
        category.save()
        return redirect('category_list')
    return render(request, 'hotel/category_form.html', {'category': category})

@login_required
def category_delete(request, id):
    category = get_object_or_404(RoomCategory, id=id)
    if request.method == 'POST':
        category.delete()
        return redirect('category_list')
    return render(request, 'hotel/category_confirm_delete.html', {'category': category})

# --- ROOM MANAGEMENT VIEWS ---
@login_required
def room_list(request):
    status_filter = request.GET.get('status', '')
    search_query = request.GET.get('q', '')
    rooms = Room.objects.all()
    if status_filter:
        rooms = rooms.filter(status=status_filter)
    if search_query:
        rooms = rooms.filter(room_number__icontains=search_query)
    return render(request, 'hotel/room_list.html', {
        'rooms': rooms,
        'status_filter': status_filter,
        'search_query': search_query
    })

@login_required
def room_add(request):
    categories = RoomCategory.objects.all()
    if request.method == 'POST':
        Room.objects.create(
            room_number=request.POST.get('room_number'),
            category_id=request.POST.get('category'),
            price=request.POST.get('price'),
            capacity=request.POST.get('capacity'),
            status=request.POST.get('status')
        )
        return redirect('room_list')
    return render(request, 'hotel/room_form.html', {'categories': categories})

@login_required
def room_edit(request, id):
    room = get_object_or_404(Room, id=id)
    categories = RoomCategory.objects.all()
    if request.method == 'POST':
        room.room_number = request.POST.get('room_number')
        room.category_id = request.POST.get('category')
        room.price = request.POST.get('price')
        room.capacity = request.POST.get('capacity')
        room.status = request.POST.get('status')
        room.save()
        return redirect('room_list')
    return render(request, 'hotel/room_form.html', {'room': room, 'categories': categories})

@login_required
def room_delete(request, id):
    room = get_object_or_404(Room, id=id)
    if request.method == 'POST':
        room.delete()
        return redirect('room_list')
    return render(request, 'hotel/room_confirm_delete.html', {'room': room})

# --- CUSTOMER MANAGEMENT VIEWS ---
@login_required
def customer_list(request):
    search_query = request.GET.get('q', '')
    customers = Customer.objects.all()
    if search_query:
        customers = customers.filter(full_name__icontains=search_query) | customers.filter(phone__icontains=search_query)
    return render(request, 'hotel/customer_list.html', {
        'customers': customers,
        'search_query': search_query
    })

@login_required
def customer_add(request):
    if request.method == 'POST':
        Customer.objects.create(
            full_name=request.POST.get('full_name'),
            phone=request.POST.get('phone'),
            email=request.POST.get('email'),
            address=request.POST.get('address', 'Hargeisa'),
            id_number=request.POST.get('id_number')
        )
        return redirect('customer_list')
    return render(request, 'hotel/customer_form.html')

@login_required
def customer_edit(request, id):
    customer = get_object_or_404(Customer, id=id)
    if request.method == 'POST':
        customer.full_name = request.POST.get('full_name')
        customer.phone = request.POST.get('phone')
        customer.email = request.POST.get('email')
        customer.address = request.POST.get('address', 'Hargeisa')
        customer.id_number = request.POST.get('id_number')
        customer.save()
        return redirect('customer_list')
    return render(request, 'hotel/customer_form.html', {'customer': customer})

@login_required
def customer_delete(request, id):
    customer = get_object_or_404(Customer, id=id)
    if request.method == 'POST':
        customer.delete()
        return redirect('customer_list')
    return render(request, 'hotel/customer_confirm_delete.html', {'customer': customer})

# --- RESERVATION MANAGEMENT VIEWS ---
@login_required
def reservation_list(request):
    reservations = Reservation.objects.all()
    return render(request, 'hotel/reservation_list.html', {'reservations': reservations})

@login_required
def reservation_add(request):
    customers = Customer.objects.all()
    available_rooms = Room.objects.filter(status='Available')
    if request.method == 'POST':
        room = get_object_or_404(Room, id=request.POST.get('room'))
        Reservation.objects.create(
            customer_id=request.POST.get('customer'),
            room=room,
            check_in_date=request.POST.get('check_in_date'),
            check_out_date=request.POST.get('check_out_date'),
            status='Booked'
        )
        room.status = 'Occupied'
        room.save()
        return redirect('reservation_list')
    return render(request, 'hotel/reservation_form.html', {
        'customers': customers,
        'rooms': available_rooms
    })

@login_required
def reservation_checkin(request, id):
    reservation = get_object_or_404(Reservation, id=id)
    reservation.status = 'Checked-In'
    reservation.save()
    return redirect('reservation_list')

@login_required
def reservation_checkout(request, id):
    reservation = get_object_or_404(Reservation, id=id)
    reservation.status = 'Checked-Out'
    reservation.save()
    reservation.room.status = 'Available'
    reservation.room.save()
    return redirect('reservation_list')