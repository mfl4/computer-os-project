class LimasSegitiga(object):
    def __init__ (self,lalas,tlimas):
        self.l= lalas
        self.t= tlimas
        pass
    def volume(self):
        V = (1 / 3) * self.l * self.t
        return V

LimasSegitiga1 = LimasSegitiga(10,12)
print("Volumenya adalah :", str(LimasSegitiga1.volume()))





