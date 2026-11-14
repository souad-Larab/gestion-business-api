""" La Class commune à tous les modèles SQLALchemy"""

from datetime import datetime, timezone
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import DateTime, func


class Base(DeclarativeBase):
    pass


class TimestampMixin:
    """ Ajoute des colonnes cree_le et modifie_le"""

   
    cree_le: Mapped [datetime] = mapped_column (
        DateTime(timezone= True) ,
        server_default= func.now()  # heure et date calculés par le serveur (la base de données)
        #default = lambda: datetime.now(timezone.utc)  | peut remplacer server_default, heure et date calculés par python  
    )

    modifie_le: Mapped[datetime] = mapped_column (
        DateTime(timezone=True),
        server_default= func.now(),
        onupdate= func.now()
    )

