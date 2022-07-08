def down(x, xmin, xmax):
    return (xmax - x) / (xmax - xmin)

def up(x, xmin, xmax):
    return (x - xmin) / (xmax - xmin)

class Kecepatan():
    minimum = 30
    middle  = 50
    maximum = 90

    def turun(self, x):
        if x >= self.maximum:
            return 0
        elif x<= self.minimum:
            return 1
        else:
            return down(x, self.minimum, self.maximum)

    def naik(self, x):
        if x >= self.maximum:
            return 1
        elif x<= self.minimum:
            return 0
        else:
            return up(x, self.minimum, self.maximum)

class Jarak():
    minimum = 5
    middle  = 15
    maximum = 20

    def sedikit(self, x):
        if x >= self.maximum:
            return 0
        elif x<= self.minimum:
            return 1
        else:
            return down(x, self.minimum, self.maximum)

    def banyak(self, x):
        if x >= self.maximum:
            return 1
        elif x<= self.minimum:
            return 0
        else:
            return up(x, self.minimum, self.maximum)


class Pengereman():
    minimum = 10%
    middle  = 50%
    maximum = 100%


    def _minimun(self, a):
        return self.maximum - a*(self.maximum - self.minimum)

    def _minimun(self, a):
        return a*(self.maximum - self.minimum) + self.minimum

    def _maximum(self, pmt=Kecepatan(), psd=Jarak()):
        result = []
        # [R1] JIKA Kecepatan Rendah, dan Jarak BANYAK, MAKA
        # Pengereman Sedikit 10%.
        a1 = min(kcp.minimum(self.kecepatan), jrk.minimum(self.jarak))
        z1 = self._minimum(a1)
        result.append((a1, z1))
        # [R2] JIKA Kecepatan RENDAH, dan Jarak PENDEK, MAKA
        # Pengereman Sedikit 10%.
        a2 = min(kcp.minimum(self.kecepatan), jrk.minimum(self.jarak))
        z2 = self._minimum(a2)
        result.append((a2, z2))
        # [R3] JIKA Kecepatan RENDAH, dan Jarak JAUH, MAKA
        # Pengeremenan Sedikit 10%.
        a3 = min(kcp.minimum(self.kecepatan), jrk.maximum(self.jarak))
        z3 = self._minimum (a3)
        result.append((a3, z3))
        # [R4] JIKA Kecepatan TINGGI, dan Jarak PENDEK, MAKA
        # Pengereman Maximum 100%.
        a4 = min(Kcp.maximum(self.kecepatan), jrk.minimum(self.jarak))
        z4 = self._maximum(a4)
        result.append((a4, z4))
        # [R5] JIKA Kecepatan Sedang, dan Jarak BANYAK, MAKA
        # Pengereman Minimum 10%
        a1 = min(kcp.middle(self.kecepatan), jrk.maximum(self.jarak))
        z1 = self._minimum(a1)
        result.append((a1, z1))
        # [R6] JIKA Kecepatan RENDAH, dan Jarak PENDEK, MAKA
        # Pengereman Middle 50%.
        a2 = min(kcp.minimum(self.kecepatan), jrk.minimum(self.jarak))
        z2 = self._minimum(a2)
        result.append((a2, z2))
        # [R7] JIKA Kecepatan Tinggi, dan Jarak JAUH, MAKA
        # Pengereman middle 50%.
        a3 = min(kcp.maximum(self.kecepatan), jrk.maximum(self.jarak))
        z3 = self._middle(a3)
        result.append((a3, z3))
        # [R8] JIKA Kecepatan TINGGI, dan Jarak PENDEK, MAKA
        # Pengereman Maximum 100%.
        a4 = min(kcp.maximum(self.kecepatan), jrk.minimum(self.jarak))
        z4 = self._maximum(a4)
        result.append((a4, z4))
        # [R9] JIKA Kecepatan SEDANG, dan Jarak PENDEK, MAKA
        # Pengereman Middle 50%.
        a3 = min(kcp.middle(self.kecepatan), jrk.minimum(self.jarak))
        z3 = self._middle(a3)
        result.append((a3, z3))
        # [R10] JIKA Kecepatan TINGGI, dan Jarak PENDEK, MAKA
        # Pengereman Maximum 100%.
        a4 = min(kcp.maximum(self.kecepatan), jrk.minimum(self.jarak))
        z4 = self._maximum(a4)
        result.append((a4, z4))
        return result
    
    def defuzifikasi(self, data_inferensi=[]):
        # (α1∗z1+α2∗z2+α3∗z3+α4∗z4) / (α1+α2+α3+α4)
        data_inferensi = data_inferensi if data_inferensi else self._inferensi()
        res_a_z = 0
        res_a = 0
        for data in data_inferensi:
            # data[0] = a 
            # data[1] = z
            res_a_z += data[0] * data[1]
            res_a += data[0]
        return res_a_z/res_a