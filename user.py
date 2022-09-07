class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name= first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0
    def display_info(self):
        list1=[self.first_name,self.last_name, self.email,self.age, self.is_rewards_member,self.gold_card_points]
        for x in list1:
            print(x)
    def enroll_self(self):
        if self.is_rewards_member == True:
            print("you are a member dingus!")
        else:
            self.is_rewards_member = True
            self.gold_card_points = 200
    def spend_points(self, points_spent):
        if self.gold_card_points >= points_spent:
            self.gold_card_points = self.gold_card_points-points_spent
        else:
            print("not enuff points friend!")


jim = User("Jim", "Jimmerson", "jim@aol.com",35)
jim.display_info()

kelly = User("kelly", "Kellerson", "kelly@netscape.com",46)
kelly.display_info()
kelly.is_rewards_member = True
kelly.enroll_self()
print(kelly.gold_card_points)
kelly.spend_points(50)
print(kelly.gold_card_points)

User.display_info
