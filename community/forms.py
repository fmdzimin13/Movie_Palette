from django import forms
from .models import Review, Comment


class ReviewForm(forms.ModelForm):
    # movie_title = forms.CharField(
    #     label='영화 제목',
    #     widget=forms.TextInput(
    #         attrs={
    #             'placeholder': '영화 제목을 작성해주세요',
    #             'maxlength': 50,
    #         }
    #     )
    # )

    title = forms.CharField(
        label='리뷰 제목',
        widget=forms.TextInput(
            attrs={
                'placeholder': '리뷰 제목을 작성해주세요',
                'maxlength': 50,
            }
        )
    )
    
    content = forms.CharField(
        label='리뷰 내용',
        widget=forms.Textarea(
            attrs={
                'placeholder': '리뷰를 작성해주세요',
                'maxlength': 200,
                'size': 10,
            }
        )
    )

    rank = forms.IntegerField(
        label='별점',
        widget=forms.NumberInput(
            attrs={
                'placeholder': '1~10점',
                'style': 'max-width: 100px;',
            }
        )
    )

    # image = forms.ImageField(
    #     label='포스터 사진',
    # )

    class Meta:
        model = Review
        exclude = ('user', 'movie', 'like_users', 'movie_title',)


class CommentForm(forms.ModelForm):
    content = forms.CharField(
        label='',
        widget=forms.TextInput(
            attrs={
                'placeholder': '댓글을 작성해주세요.',
                'maxlength': 50,
            }
        ),
    )

    class Meta:
        model = Comment
        exclude = ('review', 'user',)