from datetime import datetime
from sqlalchemy import Column, Integer, DateTime, String, JSON, ForeignKey
from sqlalchemy.orm import relationship

from database import Base

class Session(Base):
    __tablename__ = 'sessions'
    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(String, nullable=True)
    start_ts = Column(DateTime, default=datetime.utcnow, nullable=False)
    end_ts = Column(DateTime, nullable=True)
    type = Column(String, nullable=False)

    one_minute_logs = relationship('OneMinuteLog', back_populates='session')
    hot_potato_logs = relationship('HotPotatoLog', back_populates='session')
    role_play_logs = relationship('RolePlayLog', back_populates='session')

class OneMinuteLog(Base):
    __tablename__ = 'one_minute_logs'
    id = Column(Integer, primary_key=True, index=True)
    session_id = Column(Integer, ForeignKey('sessions.id'))
    topic = Column(String, nullable=False)
    highlights = Column(JSON, nullable=True)

    session = relationship('Session', back_populates='one_minute_logs')

class HotPotatoLog(Base):
    __tablename__ = 'hot_potato_logs'
    id = Column(Integer, primary_key=True, index=True)
    session_id = Column(Integer, ForeignKey('sessions.id'))
    words = Column(JSON, nullable=True)
    phrases = Column(JSON, nullable=True)

    session = relationship('Session', back_populates='hot_potato_logs')

class RolePlayLog(Base):
    __tablename__ = 'role_play_logs'
    id = Column(Integer, primary_key=True, index=True)
    session_id = Column(Integer, ForeignKey('sessions.id'))
    scenario = Column(String, nullable=False)
    roles = Column(JSON, nullable=True)
    transcript = Column(JSON, nullable=True)

    session = relationship('Session', back_populates='role_play_logs')
