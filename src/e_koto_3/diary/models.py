from django.db import models

class Post(models.Model):
    """いいことを3つ集めた日記のデータ"""

    first_text = models.CharField(max_length=25)
    second_text = models.CharField(max_length=25)
    third_text = models.CharField(max_length=25)
    date = models.DateField(auto_now=False, auto_now_add=True)

    def __str__(self):
        """表示するときに文字列で表示する"""

        return self.date.strftime('%Y/%m/%d') + 'の投稿' \
            + '\n1: ' + self.first_text \
            + '\n2: ' + self.second_text \
            + '\n3: ' + self.third_text + '\n'
            