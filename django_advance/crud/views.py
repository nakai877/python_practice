from django.views import generic
from .models import Goods
from .forms import GoodsCreateForm, GoodsUpdateForm


class GoodsCreate(generic.CreateView):
    form_class = GoodsCreateForm
    template_name = 'crud/goods_create.html'
    success_url = '/crud/goods_create'


class GoodsList(generic.ListView):
    model = Goods
    template_name = 'crud/goods_list.html'


class GoodsDetail(generic.DetailView):
    model = Goods


class GoodsUpdate(generic.UpdateView):
    model = Goods
    form_class = GoodsUpdateForm
    template_name = 'crud/goods_update.html'
    success_url = '/crud/goods_list'

class GoodsDelete(generic.DeleteView):
    # フォームは必要なし
    model = Goods
    template_name = 'crud/goods_delete.html'
    success_url = reverse_lazy('crud:goods_list')


class ImageSizeLimitationForm(forms.ModelForm):
    class Meta:
        model = Goods
        ﬁelds = ('name', 'management_code', 'price', 'release_date', 'release_ﬂag', 'description', 'image')

    def clean_image(self):
        image = self.cleaned_data.get('image', False)
        if image:
            if image.size > 10 * 1024:
                raise forms.ValidationError("ファイルサイズが大きすぎます")
        return image


class GoodsCreateWithImageSizeLimitation(generic.CreateView):
    form_class = ImageSizeLimitationForm
    template_name = 'crud/goods_create.html'
    success_url = '/crud/goods_list'
