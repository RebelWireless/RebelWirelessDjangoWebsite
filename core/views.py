from django.shortcuts import render
from .models import InternetPlan

# Create your views here.
def home(request):
    pass

def pricing(request):
    plans = InternetPlan.objects.all().order_by("base_price")

    formatted_plans = []
    for plan in plans:
        # Convert any literal "\n" to actual newlines
        description = plan.description.replace('\\n', '\n')

        formatted_plans.append({
            "title": plan.title,
            "description": description,
            "base_price": plan.base_price,
            "rental_price": plan.rental_price,
            "cta": plan.cta,
            "stats": [f.text for f in plan.all_features()],
        })

    disclaimers = [
        "* Speeds are up to advertised rates and may vary.",
        "+ Priority support available on select plans.",
        "No contracts. Cancel anytime.",
    ]

    return render(request, "core/pricing.html", {
        "plans": formatted_plans,
        "disclaimers": disclaimers,
    })
