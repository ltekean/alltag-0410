#head_page/models.py
from django.db import models
from users.models import UserModel # foreinkey 사용자 인식여부 확인


# Create your models here.
class PageModel(models.Model):
    ''' 
    컨텐츠 제목, 내용, 생성일, 수정일, 좋아요 수 
    '''
    class Meta:
        db_table = "pages"

    author = models.ForeignKey(UserModel, on_delete=models.CASCADE) # foreinkey 사용자 인식여부 확인
    title_content = models.CharField("컨텐츠 제목", max_length=256, default='None')
    text_content = models.CharField("컨텐츠 내용", max_length=1000, default='None')
    created_at = models.DateTimeField("컨텐츠 생성일", auto_now_add=True)
    updated_at = models.DateTimeField("컨텐츠 수정일", auto_now=True)
    is_liked = models.IntegerField("종아요 수")
    
    
class Isliked(models.Model):
    '''
    컨텐츠 좋아요 누르기
    '''
    pageModel = models.ForeignKey(PageModel, on_delete=models.CASCADE) # 게시글이 삭제되면 좋아요 수도 삭제한다. 
    liked_user = models.ForeignKey(UserModel.nick_name, on_delete=models.CASCADE) # user모델에서 입력받은 닉네임값을 저장
