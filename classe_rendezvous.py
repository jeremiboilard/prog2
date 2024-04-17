class Rendezvous:
    def __init__(self, p_num_rdv : int = 0, p_date_rvd : Date = None, p_heure_rdv : string = "", p_raison_rdv : string = "") :
        """
        Constructeur de la classe Rendezvous
        :param p_num_rdv: numéro du rendez-vous
        :param p_date_rvd: date du rendez-vous
        :param p_heure_rdv: heure du rendez-vous
        :param p_raison_rdv: raison du rendez-vous
        """
        self.num_rdv = p_num_rdv
        self.date_rvd = p_date_rvd
        self.heure_rdv = p_heure_rdv
        self.raison_rdv = p_raison_rdv