import random

R_EATING = "If I were you, I would go to the internet and type exactly what you wrote there!"
R_ADVICE = "If I were you, I would go to the internet and type exactly what you wrote there!"
R_BALANCE = "Here the Balance for your Account number XXXXXXXXINR send to Your Registered Mobile number through SMS"
R_TRANSTACTION = "You can Go through through the Bank number xxxxxxxxxx you get transaction details through SMS "
R_TRANSFER = "Yes, You can transfer your amount through either mode online transfer or offline transfer "
R_DO= "I can give you basic details regaring Banking of your account"


def unknown():
    response = ["Could you please re-phrase that? ",
                "...",
                "Sounds about right.",
                "What does that mean?"][
        random.randrange(4)]
    return response