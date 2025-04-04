from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Configuración de la base de datos
DATABASE_URL = "sqlite:///movimientos.db"  # Cambia la URL si usas otra base de datos
engine = create_engine(DATABASE_URL)
Base = declarative_base()
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Modelo de datos
class Movimiento(Base):
    __tablename__ = "movimientos"
    id = Column(Integer, primary_key=True, index=True)
    descripcion = Column(String, nullable=False)
    monto = Column(Float, nullable=False)
    tipo = Column(String, nullable=False)  # Ejemplo: "ingreso" o "egreso"

# Crear las tablas en la base de datos
Base.metadata.create_all(bind=engine)

# Funciones para interactuar con la base de datos
def guardar_movimiento(descripcion, monto, tipo):
    session = SessionLocal()
    try:
        nuevo_movimiento = Movimiento(descripcion=descripcion, monto=monto, tipo=tipo)
        session.add(nuevo_movimiento)
        session.commit()
    finally:
        session.close()

def obtener_movimientos():
    session = SessionLocal()
    try:
        return session.query(Movimiento).all()
    finally:
        session.close()