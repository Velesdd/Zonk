class CalcZonkCombo:

    def count_amount_each_num(self, dice_combination):
        amount_each_num = []
        for num in range(1, 7):
            amount_each_num.append(dice_combination.count(num))
        return amount_each_num

    def count_points_single_num(self, amount_each_num,dice_num):
        amount_points_single_num = 0
        if dice_num == 1:
            dice_num = 10
        if amount_each_num >= 3:
            amount_points_single_num = 10**2*dice_num
            if amount_each_num > 3:
                amount_points_single_num *= 2**(amount_each_num-3)
        else:
            if dice_num == 10 or dice_num == 5:
                amount_points_single_num += dice_num*10*amount_each_num
        return amount_points_single_num

    def count_points_each_num(self, amount_each_num):
        amount_points_each_num = []
        num = 1
        for summ in amount_each_num:
            amount_points_each_num.append(self.count_points_single_num(summ,num))
            num += 1
        return amount_points_each_num

    def count_pairs_same_num(self, amount_each_num):
        pairs = 0
        for summ in amount_each_num:
            if summ == 2:
                pairs += 1
        return pairs

    def count_total_points(self, dice_combination):
        amount_each_num = self.count_amount_each_num(dice_combination)
        if amount_each_num[0] == 1 and amount_each_num[1] == 1 and amount_each_num[2] == 1 and amount_each_num[3] == 1 and amount_each_num[4] == 1 and amount_each_num[5] == 1:
            return 1500
        if self.count_pairs_same_num(amount_each_num) == 3:
            return 750
        return sum(self.count_points_each_num(amount_each_num))
