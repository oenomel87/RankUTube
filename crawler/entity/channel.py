from sqlalchemy import Column, Integer, String, DateTime
from ..db_conn import Base

class Channel(Base()):
    __tablename__ = 'channel'

    id = Column(Integer, primary_key=True)
    channel_id = Column(String(50), unique=True, nullable=False)
    title = Column(String(255), nullable=False)
    country = Column(String(5))
    published_at = Column(DateTime)

    def __repr__(self):
        return '<Channel(id="%s", channel_id="%s", title="%s", country="%s", published_at="%s")>' \
        % (self.id, self.channel_id, self.title, self.country, self.published_at)
