from node import TwoWayNode


class BigInteger:
    def __init__(self, init_value='0'):
        self.initvalue = init_value
        self._head = TwoWayNode(init_value[-1], None, None)
        self.nodes = [self._head]
        if len(init_value) > 1:
            for x in range(-(len(init_value) - 2), 0):
                self.nodes.append(TwoWayNode(init_value[-x], init_value[-x - 1], init_value[-x + 1]))
            self.nodes.append(TwoWayNode(init_value[0], init_value[1], None))
        if init_value[0] == '-':
            self.sign = False
        else:
            self.sign = True

    def __str__(self):
        s = ''
        for item in self.nodes:
            s += item.data
        return s[::-1]

    def __eq__(self, other):
        if str(self) != str(other):
            return False
        if str(self)[0] != str(other)[0]:
            return False
        else:
            for item in range(min(len(self), len(other))):
                if self.nodes[item].data == other.nodes[item].data:
                    continue
                else:
                    return False
            return True

    def __ne__(self, other):
        if len(self) != len(other):
            return True
        elif self.sign is True and other.sign is False:
            return True
        elif self.sign is False and other.sign is True:
            return True
        else:
            for item in range(len(self)):
                if self.nodes[item].data != other.nodes[item].data:
                    return True
                else:
                    continue
            return False

    def __le__(self, other):
        if self == other:
            return True
        elif self < other:
            return True
        else:
            return False

    def __lt__(self, other):
        if self == other:
            return False
        elif str(self)[0] == '-' and str(other)[0] != '-':
            return True
        elif str(self)[0] != '-' and str(other)[0] == '-':
            return False
        elif str(self)[0] == '-' and str(other)[0] == '-':
            sf = BigInteger(str(self).replace('-', ''))
            oth = BigInteger(str(other).replace('-', ''))
            if sf > oth:
                return True
            else:
                return False
        else:
            if len(self) < len(other):
                return True
            else:
                for x in range(len(str(self))):
                    if self.nodes[x].data == other.nodes[x].data:
                        continue
                    elif self.nodes[x].data < other.nodes[x].data:
                        return True

                    return False

    def __ge__(self, other):
        if self == other:
            return True
        elif self > other:
            return True
        else:
            return False

    def __gt__(self, other):
        if self == other:
            return False
        elif str(self)[0] == '-' and str(other)[0] != '-':
            return False
        elif str(self)[0] != '-' and str(other)[0] == '-':
            return True
        elif str(self)[0] == '-' and str(other)[0] == '-':
            sf = BigInteger(str(self).replace('-', ''))
            oth = BigInteger(str(other).replace('-', ''))
            if sf > oth:
                return False
            else:
                return True
        else:
            if len(self) < len(other):
                return False
            else:
                new_oth = str(other)
                while len(str(new_oth)) < len(str(self)):
                    new_oth = '0' + new_oth
                other = BigInteger(new_oth)
                for x in range(-len(self), 0):
                    if self.nodes[x].data == other.nodes[x].data:
                        continue
                    elif self.nodes[x].data > other.nodes[x].data:
                        return True
                    continue
                return False

    def __len__(self):
        return len(self.nodes)

    def __int__(self):
        return int(str(self))

    def __repr__(self):
        return str(self)

    def __add__(self, other):
        if self.sign is False and other.sign is True:
            x = BigInteger(str(self).replace('-', ''))
            if x > other:
                return BigInteger('-'+str(x-other))
            else:
                return BigInteger(str(other-x))

        elif self.sign is True and other.sign is False:
            oth = BigInteger(str(other).replace('-', ''))
            if int(str(self)) < int(str(oth)):
                return BigInteger('-'+str(oth-self))
            elif int(str(self)) == int(str(oth)):
                return BigInteger('0')
            else:
                return self.simple_sub(oth)

        elif self.sign is True and other.sign is True:
            return self.simple_add(other)

        elif self.sign is False and other.sign is False:
            a = BigInteger(str(self).replace('-', ''))
            b = BigInteger(str(other).replace('-', ''))
            return BigInteger('-'+str(a.simple_add(b)))

    def simple_add(self, other):
        s, ost = '', 0
        new_oth = str(other)
        new_self = str(self)
        while len(str(new_oth)) < len(str(self)):
            new_oth = '0' + new_oth
        while len(new_self) != len(new_oth):
            new_self = '0' + new_self
        other = BigInteger(new_oth)
        self = BigInteger(new_self)
        for x in range(-(len(self)), 0):
            try:
                summ = int(self.nodes[x].data) + int(other.nodes[x].data) + ost
            except IndexError:
                continue
            ost = 0
            if x == -1 and str(summ)[0] != '0':
                s += str(summ)
            else:
                s += str(summ)[-1]

            if len(str(summ)) > 1:
                ost += int(str(summ)[0])
        return BigInteger(s[::-1])

    def simple_sub(self, other):
        s, ost = '', 0
        new_oth = str(other)
        while len(str(new_oth)) < len(str(self)):
            new_oth = '0' + new_oth
        oth = BigInteger(new_oth)
        for x in range(-len(self), 0):
            try:
                sub = (int(self.nodes[x].data) - ost) - int(oth.nodes[x].data)
            except IndexError:
                continue
            ost = 0
            if sub < 0:
                ost += 1
                sub = (int(self.nodes[x].data)+10) - int(oth.nodes[x].data)
            s += str(sub)[-1]
        s = s[::-1]
        while s[0] == '0' and len(s) > 2:
            s = s[1:]
        return BigInteger(s)

    def __sub__(self, other):
        if int(self) == int(other):
            return BigInteger('0')
        elif self.sign is True and other.sign is True:
            if self > other:
                return self.simple_sub(other)
            elif other > self:
                return BigInteger('-'+str(other.simple_sub(self)))

        elif self.sign is False and other.sign is False:
            sf = BigInteger(str(self).replace('-', ''))
            oth = BigInteger(str(other).replace('-', ''))
            if sf > oth:
                return BigInteger(str(oth-sf))
            else:
                return BigInteger(str(oth - sf))

        elif self.sign is True and other.sign is False:
            oth = BigInteger(str(other).replace('-', ''))
            if int(str(oth)) > int(str(self)):
                return BigInteger(str(oth+self))
            else:
                return self.simple_add(oth)

        elif self.sign is False and other.sign is True:
            a = BigInteger(str(self).replace('-', ''))
            if a < other:
                return BigInteger(str(other-a))
            else:
                return BigInteger('-'+str(a+other))

    def __mul__(self, other):
        term = int(str(other))
        res, ost = '', 0
        if term < 0:
            term = term*(-1)
            if self.sign is False:
                self = BigInteger(str(self).replace('-', ''))
            elif self.sign is True:
                self = BigInteger('-'+str(self))

        if self.sign is True:
            for x in self.nodes:
                if self.nodes.index(x) == len(self)-1:
                    res += str(int(x.data)*term + ost)[::-1]
                else:
                    m = (int(x.data)*term + ost)
                    res += str(m % 10)
                    ost = m//10
            return BigInteger(res[::-1])

        elif self.sign is False:
            for x in self.nodes:
                if self.nodes.index(x) == len(self)-2:
                    res += str(int(x.data)*term + ost)[::-1]
                    res += '-'
                    break
                else:
                    m = (int(x.data) * term + ost)
                    res += str(m % 10)
                    ost = m // 10
            return BigInteger(res[::-1])

    def _change_sign(self):
        if self.sign is True:
            return BigInteger('-'+str(self))
        else:
            return BigInteger(str(self).replace('-',''))

    def __pow__(self, power, modulo=None):
        result = BigInteger('1')
        for x in range(int(power)):
            result = BigInteger(str(result*self))
        return result

    def __floordiv__(self, other):  # //
        if str(other) == '0':
            raise ZeroDivisionError
        if int(other) == 1 and other.sign is True:
            return self
        elif int(self) == 1 and other.sign is True:
            return BigInteger('0')
        elif int(self) == 1 and other.sign is False:
            return BigInteger('-1')
        elif int(other) == 1 and other.sign is False:
            return BigInteger('-1')
        elif (self.sign and other.sign and self<other) or (self.sign is False and other.sign is False and self>other):
            return BigInteger('0')
        elif self.sign is False and int(self._change_sign()) >= int(other):
            return BigInteger('-1')
        elif self.sign is True and int(other._change_sign()) > int(self):
            return BigInteger('-1')
        probe = self
        while int(probe) > int(other):
            if probe >= other:
                probe -= other
        return probe+other


    def __truediv__(self, other):  # /
        pass


    def __mod__(self, other):
        if int(other) == 1:
            return BigInteger('0')
        if str(self) == '1' and other.sign is True:
            return BigInteger('1')
        else:
            x = self
            y = other
            if x.sign is True and y.sign is True and x < y:
                return x
            elif x.sign is False and int(BigInteger(str(x).replace('-', ''))) >= int(y):
                return BigInteger('0')
            elif x.sign is True and y.sign is False:
                probe = int(BigInteger(str(x).replace('-', '')))
                while probe >= x:
                    probe = probe.simple_sub(x)
                    # print(probe, other)
                return probe
            else:
                probe = x
                while int(probe) >= int(y):
                    probe = probe.simple_sub(y)
                return probe
            
    def _to_binary(self):
    assert int(self) >= 0
    res = "{0:b}".format(int(self))
    return BigInteger(res)

    def __xor__(self, other):  # ^
        self_bin = self._to_binary()
        other_bin = str(other._to_binary())
        while len(other_bin) < len(self_bin):
            other_bin = '0' + str(other_bin)
        other_bin = BigInteger(other_bin)
        y = int(str(self_bin), 2) ^ int(str(other_bin), 2)
        res = bin(y)[2:].zfill(len(self_bin))
        return BigInteger(res)._from_bin()
    def __and__(self, other):  # &
        pass

    def __lshift__(self, other):  # <<
        pass

    def __rshift__(self, other):  # >>
        pass
